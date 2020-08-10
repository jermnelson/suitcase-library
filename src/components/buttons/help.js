import React from "react"

import ReferenceHelpIcon from "../../images/ReferenceHelpIcon.png"

const ReferenceHelp = () => {

  const handleClick = () => {
   return (prompt('What is your question?'))

  }

  return(
   <button href="#" onClick={handleClick}>
     <img alt="Reference Help" src={ReferenceHelpIcon} /> 
   </button>
  )
}

export default ReferenceHelp
