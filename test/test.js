
const {keyListener} = require('../keylistener')

const listener = keyListener((data) => {
  if (data.key == 'esc') listener.kill()
  else console.log(data)
})
