function Hands(props){
    if(props.list.length == 0)
        return <></>
    let list = []
    const regex = /\B[A-Z]/ //matches all uppercase letters not on boundary
    props.list.forEach((e) =>{
        Object.keys(e).forEach((key) =>{
            let index = key.search(regex)
            let new_key = key.replace(regex, " " + key.charAt(index))
            list.push(new_key.replace("ofa", " of a") + ": " + e[key])
        })
    })
    return list.map((e, index) => {
        return <p key={index} className="hands">{e}</p>
    })
}

export default Hands