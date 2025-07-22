import { useState } from 'react'
import './App.css'
import { uploadFile } from './services/api'

function App() {

  return (
    <>
      <form action={uploadFile}>
        <input type="file" name="profile" accept=".jkr"/>
        <input type="submit" value={"Upload file"}/>
        <br />
        <span id='file1'></span>
      </form>
    </>
  )
}

export default App
