import { useEffect, useState, useActionState } from 'react'
import './css/App.css'
import { uploadFile, removeFile, toggleFile, getList } from './services/api'
import DisplayList from './components/DisplayList';

function App() {
  const total = 4

  const [displayList, setDisplayList] = useState({list:[], item:"career"});
  const [firstRender, setFirstRender] = useState(true);
  const [fileUploaded, setFileUploaded] = useState({bool:false, num:0});
  const [filesToggled, setFilesToggled] = useState([]);

  const[returnState, formAction] = useActionState(uploadFile, undefined);

 useEffect (() => {
    if(!firstRender)
      setDisplayList({list: returnState, item: displayList.item})
    setFirstRender(false)
  }, [returnState])

  useEffect (() => {
    if(firstRender && document.getElementById("#file1") && document.getElementById("#file2") && document.getElementById("#file3")){
      for(let i = 1; i <= 3; i++){
        document.getElementById(`label${i}`).style.background = "rgb(46,118,253)"
        document.getElementById(`file${i}`).removeAttribute("disabled")
        document.getElementById(`remove${i}`).style.background = "grey"
        document.getElementById(`remove${i}`).setAttribute("disabled", "")
      }
    }
    if(!firstRender){
      if(fileUploaded.bool){
        document.getElementById(`label${fileUploaded.num}`).style.background = "grey"
        document.getElementById(`file${fileUploaded.num}`).setAttribute("disabled", "")
        document.getElementById(`remove${fileUploaded.num}`).style.background = "rgb(255, 68, 59)"
        document.getElementById(`remove${fileUploaded.num}`).removeAttribute("disabled")
      }
      else {
        document.getElementById(`label${fileUploaded.num}`).style.background = "rgb(46,118,253)"
        document.getElementById(`file${fileUploaded.num}`).removeAttribute("disabled")
        document.getElementById(`remove${fileUploaded.num}`).style.background = "grey"
        document.getElementById(`remove${fileUploaded.num}`).setAttribute("disabled", "")
      }
    }
  }, [fileUploaded])

  useEffect (() => {
    if(!firstRender){
      for(let i = 1; i <= 3; i++){
        if(filesToggled.includes(i)){
          document.getElementById(`save${i}`).style.background = "grey"
        }
        else{
          document.getElementById(`save${i}`).style.background = "rgb(255, 68, 59)"
        }
      }
    }
  }, [filesToggled])

  useEffect (() => {
    if(document.querySelector(".marker")){
      let list = document.querySelectorAll("nav button")
      let index = ""
      if(displayList.item == "career"){
        index = 0
      }
      else if(displayList.item == "hands"){
        index = 1
      }
      else if(displayList.item == "decks"){
        index = 2
      }
      else if(displayList.item == "jokers"){
        index = 3
      }
      else if(displayList.item == "consumables"){
        index = 4
      }
      else if(displayList.item == "tarots"){
        index = 5
      }
      else if(displayList.item == "planets"){
        index = 6
      }
      else if(displayList.item == "spectrals"){
        index = 7
      }
      else if(displayList.item == "vouchers"){
        index = 8
      }
      if(!firstRender){
        let buttonRect = list[index].getBoundingClientRect()
        let displayRect = document.querySelector("#display").getBoundingClientRect()
        document.querySelector(".marker").style.left = `${(buttonRect.left - displayRect.left)}px`
        document.querySelector(".marker").style.marginLeft = `${(buttonRect.right - buttonRect.left - 40)/2}px` //convert to %
        document.querySelector(".marker").style.marginRight = `${(buttonRect.right - buttonRect.left - 40)/2}px`
      }
      
    }
    
  }, [displayList.item])
  
  return (
    <>
      <h1>Balatro Stat Compiler</h1>
      <div id='fileInput'>
        <div>
          <button className="save" id="save1" onClick={() => {
            if(filesToggled.includes(1)){
              let newList = [...filesToggled]
              newList.splice(newList.indexOf(1), 1)
              setFilesToggled(newList)
              toggleFile(1, 1, displayList.item).then((rsp) => setDisplayList({list: rsp, item: displayList.item}))
            }
            else{
              let newList = [...filesToggled]
              newList.push(1)
              setFilesToggled(newList)
              toggleFile(0, 1, displayList.item).then((rsp) => setDisplayList({list: rsp, item: displayList.item}))
            }
          }}>Save 1</button>
          <form action={(e) =>{
            e.append("fileNum", 1)
            e.append("itemType", displayList.item)
            setFileUploaded({bool: true, num: 1})
            formAction(e)}} id="fileForm1">
            <label id="label1" htmlFor="file1">Upload</label>
            <input type="file" name="profile" accept=".jkr" id='file1' onChange={() =>{
              if(document.getElementById("fileForm1")){
                fileForm1.requestSubmit()
              }
            }}/>
            {/* set inner html to remove1 on file upload and browse when removed */}
            <span id='fileSpan1'></span>
          </form>
          <button id='remove1' onClick={() => {
            removeFile(1, displayList.item).then((rsp) => setDisplayList({list: rsp, item: displayList.item}))
            setFileUploaded({bool: false, num: 1})
            }}>Remove</button>
        </div>
        
      

        <div>
          <button className="save" id="save2" onClick={() => {
            if(filesToggled.includes(2)){
              let newList = [...filesToggled]
              newList.splice(newList.indexOf(2), 1)
              setFilesToggled(newList)
              toggleFile(1, 2, displayList.item).then((rsp) => setDisplayList({list: rsp, item: displayList.item}))
            }
            else{
              let newList = [...filesToggled]
              newList.push(2)
              setFilesToggled(newList)
              toggleFile(0, 2, displayList.item).then((rsp) => setDisplayList({list: rsp, item: displayList.item}))
            }
          }}>Save 2</button>
          <form action={(e) =>{
            e.append("fileNum", 2)
            e.append("itemType", displayList.item)
            setFileUploaded({bool: true, num: 2})
            formAction(e)}} id="fileForm2">
            <label id="label2" htmlFor="file2">Upload</label>
            <input type="file" name="profile" accept=".jkr" id='file2' onChange={() =>{
              if(document.getElementById("fileForm2"))
                fileForm2.requestSubmit()
            }}/>
          <span id='fileSpan2'></span>
          </form>
          <button id='remove2' onClick={() => {
            removeFile(2, displayList.item).then((rsp) => setDisplayList({list: rsp, item: displayList.item}))
            setFileUploaded({bool: false, num: 2})
            }}>Remove</button>
        </div>
        
      
      
        <div>
          <button className="save" id="save3" onClick={() => {
            if(filesToggled.includes(3)){
              let newList = [...filesToggled]
              newList.splice(newList.indexOf(3), 1)
              setFilesToggled(newList)
              toggleFile(1, 3, displayList.item).then((rsp) => setDisplayList({list: rsp, item: displayList.item}))
            }
            else{
              let newList = [...filesToggled]
              newList.push(3)
              setFilesToggled(newList)
              toggleFile(0, 3, displayList.item).then((rsp) => setDisplayList({list: rsp, item: displayList.item}))
            }
          }}>Save 3</button>
          <form action={(e) =>{
            e.append("fileNum", 3)
            e.append("itemType", displayList.item)
            setFileUploaded({bool: true, num: 3})
            formAction(e)}} id="fileForm3">
            <label id="label3" htmlFor="file3">Upload</label>
            <input type="file" name="profile" accept=".jkr" id='file3' onChange={() =>{
              if(document.getElementById("fileForm3"))
                fileForm3.requestSubmit()
            }}/>
            <span id='fileSpan3'></span>
          </form>
          <button id='remove3' onClick={() => {
            removeFile(3, displayList.item).then((rsp) => setDisplayList({list: rsp, item: displayList.item}))
            setFileUploaded({bool: false, num: 3})
        }}>Remove</button>
        </div>
      </div>
      
      <div id='display'>
        <img src="/images/arrow.svg" alt="" className="marker"/>
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
        <DisplayList list={displayList.list} item={displayList.item} bool={fileUploaded.bool}/>
      </div>
      
      <div id="footer">
        
          <p>All assets used are property of LocalThunk and Playstack. m6x11 font by: <a href="https://managore.itch.io/m6x11">Daniel Linssen</a></p>
          <a href="https://github.com/jrw567/Balatro-Stat-Compiler">View code on GitHub</a>
          
      </div>
    </>
    
  )
}

export default App
