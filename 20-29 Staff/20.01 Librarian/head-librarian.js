import React from "react"
import { Link } from "gatsby"

import Layout from "../../components/layout"
import Portrait from "../../images/HeadLibrarian.png"

const HeadLibrarian = () => {
 
  const answerQuestion = (event) => {
    alert(`Your question`)

  }

  return (
    <div className="wrapper window staff">
      <div class="title-bar">
        <div class="title-bar-text">Ms. Eliza, Head Librarian</div>
      </div>
      <div className="window-body">
       <h2 className="staff-title">Head Librarian</h2>
       <div className="staff-profile">
         <div className="staff-photo">
           <img src={Portrait} className="headshot" alt="Head Librarian Portrait" />
         </div>
         <div className="staff-info">
           <h3>About</h3>
             <fieldset>
                <legend>How can I help?</legend>
                <div className="field-row">
                    <label>Enter your question</label>
                    <input type="text" style={{width: "300px"}} name="" />
                    <button onClick={answerQuestion}>Go</button> 
                </div>
             </fieldset>
         </div>
         <div></div>
       </div>
     </div>
    </div>
  )
}

export default HeadLibrarian 
