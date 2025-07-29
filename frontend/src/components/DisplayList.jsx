function DisplayList(displayList, displayItem){
    if(displayList.list.length == 0)
        return <></>
    let list = []
    Object.keys(displayList.list[0]).forEach((key) =>{
        list.push(key.replace(/_/g, " ") + ": " + displayList.list[0][key])
    })
    return list.map((e, index) => {
        console.log(e)
        return <p key={index} className="career">{e}</p>
    })
}

export default DisplayList