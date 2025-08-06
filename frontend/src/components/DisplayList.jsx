import Career from "./Career"
import Deck from "./Deck"
import Joker from "./Joker"
import Other from "./Other"

function DisplayList(props){
    if(props.list.length == 0 || props.item == null)
        return <></>
    if(props.item == "career")
        return <Career list={props.list}/>
    else if(props.item == "decks")
        return <Deck list={props.list}/>
    else if(props.item == "jokers")
        return <Joker list={props.list}/>
     else if(props.item == "hands" || props.item == "consumables" || props.item == "tarots" || props.item == "planets" || props.item == "spectrals" || props.item == "vouchers")
        return <Other list={props.list} item={props.item}/>
    else {
        return <p className="error">An error has occurred. Please reload the site.</p>
    }
}

export default DisplayList