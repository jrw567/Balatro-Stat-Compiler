import { useState } from 'react'
import './App.css'
import { uploadFile1, uploadFile2, uploadFile3 } from './services/api'

function App() {

  return (
    <>
    {/* unhappy with this implementation will make generic upload file */}
      <form action={uploadFile1}>
        <input type="file" name="profile" accept=".jkr"/>
        <input type="submit" value={"Upload file"}/>
        <br />
        <span id='file1'></span>
      </form>

      <form action={uploadFile2}>
        <input type="file" name="profile" accept=".jkr"/>
        <input type="submit" value={"Upload file"}/>
        <br />
        <span id='file2'></span>
      </form>

      <form action={uploadFile3}>
        <input type="file" name="profile" accept=".jkr"/>
        <input type="submit" value={"Upload file"}/>
        <br />
        <span id='file3'></span>
      </form>
    </>
  )
}

export default App
