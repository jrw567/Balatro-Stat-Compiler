import Career from "./Career"
import Hands from "./Hands"
import Deck from "./Deck"

function DisplayList(props){
    if(props.list.length == 0 || props.item == null)
        return <></>
    if(props.item == "career")
        return <Career list={props.list}/>
    else if(props.item == "hands")
        return <Hands list={props.list}/>
    else if(props.item == "decks")
        return <Deck list={props.list}/>
}

export default DisplayList