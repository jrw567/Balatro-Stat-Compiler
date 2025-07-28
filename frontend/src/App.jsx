import { useEffect, useState, useActionState } from 'react'
import './App.css'
import { uploadFile, removeFile, getList } from './services/api'

function App() {
  const [displayList, setDisplayList] = useState([]);
  const [displayItem, setDisplayItem] = useState("career");
  const [firstRender, setFirstRender] = useState(true);

  const[state, formAction] = useActionState(uploadFile, undefined);

  useEffect (() => {
    document.getElementById("fileForm1").addEventListener('formdata', (e) => {
      e.formData.append("fileNum", 1)
      e.formData.append("itemType", displayItem)});

    document.getElementById("fileForm2").addEventListener('formdata', (e) => {
      e.formData.append("fileNum", 2)
      e.formData.append("itemType", displayItem)});

    document.getElementById("fileForm3").addEventListener('formdata', (e) => {
      e.formData.append("fileNum", 3)
      e.formData.append("itemType", displayItem)});

    document.getElementById("remove1").addEventListener('click', () => {removeFile(1)});
    document.getElementById("remove2").addEventListener('click', () => {removeFile(2)});
    document.getElementById("remove3").addEventListener('click', () => {removeFile(3)});

    setFirstRender(false);
  }, [])

  useEffect (() => {
    console.log(firstRender)
    if(!firstRender)
      setDisplayList("Hello")
  }, [state])

  
  return (
    <>
    {/* unhappy with this implementation will make generic upload file */}
      <form action={formAction} id="fileForm1">
        <input type="file" name="profile" accept=".jkr"/>
        <input type="submit" value={"Upload file"}/>
        <br />
        <span id='file1'></span>
      </form>
      <button id='remove1'>Remove</button>

      <form action={formAction} id="fileForm2">
        <input type="file" name="profile" accept=".jkr"/>
        <input type="submit" value={"Upload file"}/>
        <br />
        <span id='file2'></span>
      </form>
      <button id='remove2'>Remove</button>

      <form action={formAction} id="fileForm3">
        <input type="file" name="profile" accept=".jkr"/>
        <input type="submit" value={"Upload file"}/>
        <br />
        <span id='file3'></span>
      </form>
      <button id='remove3'>Remove</button>

      <div>
        <p>{displayList}</p>
      </div>
    </>
    
  )
}

export default App
