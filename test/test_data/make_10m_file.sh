#!/usr/bin/env bash
set -Ceu
#---------------------------------------------------------------------------
# 10MBのファイルを作成する。10MBははてなフォトライフにおけるサイズ上限。
# CreatedAt: 2021-10-08
#---------------------------------------------------------------------------
Run() {
	THIS="$(realpath "${BASH_SOURCE:-0}")"; HERE="$(dirname "$THIS")"; PARENT="$(dirname "$HERE")"; THIS_NAME="$(basename "$THIS")"; APP_ROOT="$PARENT";
	cd "$HERE"
	dd if=/dev/zero of=over_size.png bs=1M count=10
}
Run "$@"
