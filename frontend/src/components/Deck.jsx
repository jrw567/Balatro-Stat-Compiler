function Deck(props){
    if(props.list.length == 0)
        return <></>
    let list = []
    const regex = /\B[A-Z]/ //matches all uppercase letters not on boundary
    let list_json = JSON.stringify(props.list)
    props.list.forEach((e) =>{
         Object.keys(e).forEach((key) =>{
            // console.log(list_json.map(x => x[key]))
        })
    })
    return list.map((e, index) => {
        return <p key={index} className="decks">{e}</p>
    })
}
export default Deck