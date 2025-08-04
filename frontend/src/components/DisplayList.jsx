import Career from "./Career"
import Hands from "./Hands"
import Deck from "./Deck"
import Joker from "./Joker"

function DisplayList(props){
    if(props.list.length == 0 || props.item == null)
        return <></>
    if(props.item == "career")
        return <Career list={props.list}/>
    else if(props.item == "hands")
        return <Hands list={props.list}/>
    else if(props.item == "decks")
        return <Deck list={props.list}/>
    else if(props.item == "jokers")
        return <Joker list={props.list}/>
     else if(props.item == "consumables")
        console.log(props.list)
        //return <Joker list={props.list}/>
}

export default DisplayList