#!/usr/bin/bash
# Install the last Rust Cargo Project Manager
curl --proto "=https" --tlsv1.2 -sSf https://sh.rustup.rs | sh
# Build Project
~/cargo/bin/cargo build