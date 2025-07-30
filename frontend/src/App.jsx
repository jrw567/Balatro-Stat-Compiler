import { useEffect, useState, useActionState } from 'react'
import './App.css'
import { uploadFile, removeFile, getList } from './services/api'
import DisplayList from './components/DisplayList';

function App() {
  const [displayList, setDisplayList] = useState([]);
  const [displayItem, setDisplayItem] = useState("career");
  const [firstRender, setFirstRender] = useState(true);
  const total = 1 //change to 4*******

  const[returnState, formAction] = useActionState(uploadFile, undefined);

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
    if(!firstRender)
      setDisplayList(returnState)
  }, [returnState])

  useEffect (() => {
    if(!firstRender)
      setDisplayList(getList(total, displayItem))
  }, [displayItem])

  
  return (
    <>
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
      <br />

    <nav>
      <button onClick={() => setDisplayItem("career")}>Career Stats</button>
      <button>Hand Stats</button>
      <button>Deck Stats</button>
      <button>Jokers</button>
      <button>Consumables</button>
      <button>Tarots</button>
      <button>Planets</button>
      <button>Spectrals</button>
      <button>Vouchers</button>
    </nav>
      <br />
      <DisplayList list={displayList} item={displayItem}/>
    </>
    
  )
}

export default App
