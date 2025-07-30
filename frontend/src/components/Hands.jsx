function Hands(props){
    if(props.list.length == 0)
        return <></>
    let list = []
    props.list.forEach((e) =>{
        Object.keys(e).forEach((key) =>{
        list.push(key + ": " + e[key])
        console.log(e[key])
        })
    })
    return list.map((e, index) => {
        return <p key={index} className="hands">{e}</p>
    })
}

export default Hands