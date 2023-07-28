const { execFile } = require('child_process')


function keyListener(callback) {
  const child = execFile('./dist/main.exe')
  child.stdout.on('data', (data) => {
    callback(JSON.parse(data.toString()))
  })
  return child
}

module.exports = (keyListener)
