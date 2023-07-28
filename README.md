# keylistener
A global keylistener for Node.js created using python.
## Usage
#### Importing keyListener
```js   
const {keyListener} = require('./keylistener')
```
#### How it works?
Keylistener runs a child process which was created using keyboard module in python and built using pyinstaller.   
The function `keyListener` returns a Node.js `ChildProcess`
