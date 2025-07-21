import { useState } from 'react'
import './App.css'
import { uploadFile } from './services/api'

function App() {

  return (
    <>
      <form action={uploadFile}>
        <input type="file" name="profile" accept=".jkr"/>
        <input type="submit" />
      </form>
    </>
  )
}

export default App
