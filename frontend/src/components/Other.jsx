// component used to represent Hands, Consumables, Tarots, Planets, Spectrals, and Vouchers since they are all represented by name and count
function Other(props){
    if(props.list.length == 0)
        return <></>
    let list = []
    const under_regex = /_/g //matches all underscores
    const name_regex = /\b[a-z]/ //matches first letters of a word that are lowercase
    const hand_regex = /\B[A-Z]/ //matches all uppercase letters not on boundary
    props.list.forEach((e) =>{
        let other = e.name
        let count = e.count
        other = other.replace(under_regex, " ")
        if(props.item == "hands"){
            let index = other.search(hand_regex)
            other = other.replace(hand_regex, " " + other.charAt(index)).replace("ofa", " of a")
        }
        else {
            while(other.search(name_regex) >= 0){
                other = other.replace(name_regex, char => char.toUpperCase())
            }
        }
        list.push(other + `: Count: ${count}`)
    })
    return list.map((e, index) => {
        return <p key={index} className={props.item}>{e}</p>
    })
}
export default Other