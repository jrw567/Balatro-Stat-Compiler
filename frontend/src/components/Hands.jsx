function Hands(props){
    if(props.list.length == 0)
        return <></>
    let list = []
    const regex = /\B[A-Z]/ //matches all uppercase letters not on boundary
    props.list.forEach((e) =>{
        let hand = e.name
        let count = e.count
        let index = hand.search(regex)

        hand = hand.replace(regex, " " + hand.charAt(index)).replace("ofa", " of a")
        list.push(hand + ": " + count)
    })
    return list.map((e, index) => {
        return <p key={index} className="hands">{e}</p>
    })
}

export default Hands