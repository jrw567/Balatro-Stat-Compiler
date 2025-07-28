import { useEffect, useState } from 'react'
import './App.css'
import { uploadFile1, uploadFile2, uploadFile3, removeFile, getList } from './services/api'

function App() {
  const [displayList, setDisplayList] = useState([]);
  const [displayItem, setDisplayItem] = useState("career");
  useEffect (() => {
    document.getElementById("delete1").addEventListener('click', () => {removeFile(1)});
    document.getElementById("delete2").addEventListener('click', () => {removeFile(2)});
    document.getElementById("delete3").addEventListener('click', () => {removeFile(3)});
  }, [])
  
  return (
    <>
    {/* unhappy with this implementation will make generic upload file */}
      <form action={uploadFile1}>
        <input type="file" name="profile" accept=".jkr"/>
        <input type="submit" value={"Upload file"}/>
        <br />
        <span id='file1'></span>
      </form>
      <button id='delete1'>Delete</button>
      <form action={uploadFile2}>
        <input type="file" name="profile" accept=".jkr"/>
        <input type="submit" value={"Upload file"}/>
        <br />
        <span id='file2'></span>
      </form>
      <button id='delete2'>Delete</button>

      <form action={uploadFile3}>
        <input type="file" name="profile" accept=".jkr"/>
        <input type="submit" value={"Upload file"}/>
        <br />
        <span id='file3'></span>
      </form>
      <button id='delete3'>Delete</button>

      <div>
        <p>{displayList}</p>
      </div>
    </>
    
  )
}

export default App
