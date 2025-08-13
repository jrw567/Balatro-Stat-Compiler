import Career from "./Career"
import Deck from "./Deck"
import Joker from "./Joker"
import Other from "./Other"
import "../css/DisplayList.css"

function DisplayList(props){
    if(props.list == null || props.item == null|| props.list.length == 0)
        return <div id="displayBox">
            <p>Insert description of how the application works</p>
        </div>
    if(props.item == "career")
        return <div id="displayBox"><Career list={props.list}/></div>
    else if(props.item == "decks")
        return <div id="displayBox"><Deck list={props.list}/></div>
    else if(props.item == "jokers")
        return <div id="displayBox"><Joker list={props.list}/></div>
     else if(props.item == "hands" || props.item == "consumables" || props.item == "tarots" || props.item == "planets" || props.item == "spectrals" || props.item == "vouchers")
        return <div id="displayBox"><Other list={props.list} item={props.item}/></div>
    else {
        return <div id="displayBox"><p className="error">An error has occurred. Please reload the site.</p></div>
    }
}

export default DisplayList