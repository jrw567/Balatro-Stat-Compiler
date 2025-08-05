function Consumable(props){
    if(props.list.length == 0)
        return <></>
    let list = []
    const regex = /_/g //matches all underscores
    props.list.forEach((e) =>{
        let consumable = e.name
        let count = e.count
        consumable = consumable.replace(consumable.charAt(0), consumable.charAt(0).toUpperCase()).replace(regex, " ")
        list.push(consumable + `: Count: ${count}`)
    })
    return list.map((e, index) => {
        return <p key={index} className={props.item}>{e}</p>
    })
}
export default Consumable