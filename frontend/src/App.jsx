import { useEffect, useState, useActionState } from 'react'
import './css/App.css'
import { uploadFile, removeFile, getList } from './services/api'
import DisplayList from './components/DisplayList';

function App() {
  const total = 4

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
      <h1>Balatro Stat Compiler</h1>
      <div id='fileInput'>
        <div>
          <button className="save">Save 1</button>
          <form action={(e) =>{e.append("fileNum", 1), e.append("itemType", displayList.item), formAction(e)}} id="fileForm1">
            <label htmlFor="file1">Upload</label>
            <input type="file" name="profile" accept=".jkr" id='file1' onChange={() =>{
              if(document.getElementById("fileForm1"))
                fileForm1.requestSubmit()
            }}/>
            {/* set inner html to remove1 on file upload and browse when removed */}
            <span id='fileSpan1'></span>
          </form>
          <button className='remove' onClick={() => {removeFile(1, displayList.item).then((rsp) => setDisplayList({list: rsp, item: displayList.item}))}}>Remove</button>
        </div>
        
      

        <div>
          <button className="save">Save 2</button>
          <form action={(e) =>{e.append("fileNum", 2), e.append("itemType", displayList.item), formAction(e)}} id="fileForm2">
            <label htmlFor="file2">Upload</label>
            <input type="file" name="profile" accept=".jkr" id='file2' onChange={() =>{
              if(document.getElementById("fileForm2"))
                fileForm2.requestSubmit()
            }}/>
          <span id='fileSpan2'></span>
          </form>
          <button className='remove' onClick={() => {removeFile(2, displayList.item).then((rsp) => setDisplayList({list: rsp, item: displayList.item}))}}>Remove</button>
        </div>
        
      
      
        <div>
          <button className="save">Save 3</button>
          <form action={(e) =>{e.append("fileNum", 3), e.append("itemType", displayList.item), formAction(e)}} id="fileForm3">
            <label htmlFor="file3">Upload</label>
            <input type="file" name="profile" accept=".jkr" id='file3' onChange={() =>{
              if(document.getElementById("fileForm3"))
                fileForm3.requestSubmit()
            }}/>
            <span id='fileSpan3'></span>
          </form>
          <button className='remove' onClick={() => {removeFile(3, displayList.item).then((rsp) => setDisplayList({list: rsp, item: displayList.item}))}}>Remove</button>
        </div>
      </div>
      
      <div id='display'>
        <nav>
          <button onClick={() => { getList(total, "career").then((rsp) => setDisplayList({list: rsp, item:"career"}))}}>Career Stats</button>
          <button onClick={() => { getList(total, "hands").then((rsp) => setDisplayList({list: rsp, item:"hands"}))}}>Hand Stats</button>
          <button onClick={() => { getList(total, "decks").then((rsp) => setDisplayList({list: rsp, item:"decks"}))}}>Deck Stats</button>
          <button onClick={() => { getList(total, "jokers").then((rsp) => setDisplayList({list: rsp, item:"jokers"}))}}>Jokers</button>
          <button onClick={() => { getList(total, "consumables").then((rsp) => setDisplayList({list: rsp, item:"consumables"}))}}>Consumables</button>
          <button onClick={() => { getList(total, "tarots").then((rsp) => setDisplayList({list: rsp, item:"tarots"}))}}>Tarots</button>
          <button onClick={() => { getList(total, "planets").then((rsp) => setDisplayList({list: rsp, item:"planets"}))}}>Planets</button>
          <button onClick={() => { getList(total, "spectrals").then((rsp) => setDisplayList({list: rsp, item:"spectrals"}))}}>Spectrals</button>
          <button onClick={() => { getList(total, "vouchers").then((rsp) => setDisplayList({list: rsp, item:"vouchers"}))}}>Vouchers</button>
        </nav>
        <DisplayList list={displayList.list} item={displayList.item}/>
      </div>
      
      <div id="footer">
        
          <p>All assets used are property of LocalThunk and Playstack. m6x11 font by: <a href="https://managore.itch.io/m6x11">Daniel Linssen</a></p>
          <a href="https://github.com/jrw567/Balatro-Stat-Compiler">View code on GitHub</a>
          
      </div>
    </>
    
  )
}

export default App
