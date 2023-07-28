# keylistener
A global keylistener for Node.js created using python.
## Usage
#### Importing keyListener
```js   
const {keyListener} = require('./keylistener')
```
#### Creating a keyListener
The `keyListener` function takes a callback function as an argument and returns a Node.js `ChildProcess`.   
The process can be killed using `<processname>.kill()`. Refer to `/test/test.js` for an example.
## How it works?
Keylistener runs a child process which was created using keyboard module in python and built using pyinstaller.
