function Career(props){
    if(props.list.length == 0)
        return <></>
    let list = []
    Object.keys(props.list[0]).forEach((key) =>{
        list.push(key.replace(/_/g, " ") + ": " + props.list[0][key])
    })
    return list.map((e, index) => {
        return <p key={index} className="career">{e}</p>
    })
}
export default Career