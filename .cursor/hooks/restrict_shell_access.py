#!/usr/bin/env python3

import json
import os
import shlex
import sys


BLOCKED_SHELLS = {"bash", "sh", "zsh", "dash", "ksh"}


def emit(permission, user_message=None, agent_message=None):
    response = {"permission": permission}
    if user_message:
        response["userMessage"] = user_message
    if agent_message:
        response["agentMessage"] = agent_message

    sys.stdout.write(json.dumps(response))


def resolve_invoked_command(args):
    if not args:
        return "", ""

    command = os.path.basename(args[0])
    if command != "env":
        return command, args[0]

    for token in args[1:]:
        if "=" in token and token.split("=", 1)[0].isidentifier():
            continue
        return os.path.basename(token), token

    return command, args[0]


def main():
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        emit(
            "deny",
            "Shell command blocked because the policy payload was invalid.",
            "The beforeShellExecution hook received invalid JSON. Do not retry until the hook is fixed.",
        )
        return 2

    command = (payload.get("command") or "").strip()
    if not command:
        emit("allow")
        return 0

    try:
        args = shlex.split(command, posix=True)
    except ValueError:
        emit(
            "deny",
            "Shell command blocked because it could not be parsed safely.",
            "The proposed shell command could not be parsed safely by project policy.",
        )
        return 2

    invoked_command, raw_command = resolve_invoked_command(args)
    if invoked_command in BLOCKED_SHELLS:
        emit(
            "deny",
            "Direct shell access is restricted for this project.",
            f"Blocked shell invocation `{raw_command}` by project policy. Use approved non-shell tools or a permitted command instead.",
        )
        return 2

    emit("allow")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
