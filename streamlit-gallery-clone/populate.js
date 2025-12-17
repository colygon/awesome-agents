import { spawn } from 'node:child_process';

// Back-compat: populate now delegates to the configurable sync pipeline.
const child = spawn(process.execPath, ['sync.js', '--config', './sync.config.example.json'], {
  stdio: 'inherit'
});

child.on('exit', code => {
  process.exitCode = code ?? 1;
});
