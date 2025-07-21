import { useState } from 'react'
import './App.css'

function App() {

  return (
    <>
      <form action="http://localhost:5000" method="POST" encType="multipart/form-data">
        <input type="file" name="profile" accept=".jkr"/>
        <input type="submit" />
      </form>
    </>
  )
}

export default App
