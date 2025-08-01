import { useEffect, useState, useActionState } from 'react'
import './App.css'
import { uploadFile, removeFile, getList } from './services/api'
import DisplayList from './components/DisplayList';

function App() {
  const total = 1 //change to 4*******

  const [displayList, setDisplayList] = useState({list:[], item:"career"});
  const [firstRender, setFirstRender] = useState(true);

  const[returnState, formAction] = useActionState(uploadFile, undefined);

  useEffect (() => {
    if(!firstRender)
      setDisplayList({list: returnState, item: displayList.item})
    setFirstRender(false)
  }, [returnState])
  
  return (
    <>
      <form action={(e) =>{e.append("fileNum", 1), e.append("itemType", displayList.item), formAction(e)}} id="fileForm1">
        <input type="file" name="profile" accept=".jkr"/>
        <input type="submit" value={"Upload file"}/>
        <br />
        <span id='file1'></span>
      </form>
      <button id='remove1' onClick={() => {removeFile(1, displayList.item).then((rsp) => setDisplayList({list: rsp, item: displayList.item}))}}>Remove</button>

      <form action={(e) =>{e.append("fileNum", 2), e.append("itemType", displayList.item), formAction(e)}} id="fileForm2">
        <input type="file" name="profile" accept=".jkr"/>
        <input type="submit" value={"Upload file"}/>
        <br />
        <span id='file2'></span>
      </form>
      <button id='remove2' onClick={() => {removeFile(2, displayList.item).then((rsp) => setDisplayList({list: rsp, item: displayList.item}))}}>Remove</button>

      <form action={(e) =>{e.append("fileNum", 3), e.append("itemType", displayList.item), formAction(e)}} id="fileForm3">
        <input type="file" name="profile" accept=".jkr"/>
        <input type="submit" value={"Upload file"}/>
        <br />
        <span id='file3'></span>
      </form>
      <button id='remove3' onClick={() => {removeFile(3, displayList.item).then((rsp) => setDisplayList({list: rsp, item: displayList.item}))}}>Remove</button>
      <br />

    <nav>
      <button onClick={() => { getList(total, "career").then((rsp) => setDisplayList({list: rsp, item:"career"}))}}>Career Stats</button>
      <button onClick={() => { getList(total, "hands").then((rsp) => setDisplayList({list: rsp, item:"hands"}))}}>Hand Stats</button>
      <button onClick={() => { getList(total, "decks").then((rsp) => setDisplayList({list: rsp, item:"decks"}))}}>Deck Stats</button>
      <button>Jokers</button>
      <button>Consumables</button>
      <button>Tarots</button>
      <button>Planets</button>
      <button>Spectrals</button>
      <button>Vouchers</button>
    </nav>
      <br />
      <DisplayList list={displayList.list} item={displayList.item}/>
    </>
    
  )
}

export default App
