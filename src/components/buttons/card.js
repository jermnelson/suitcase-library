import React from "react"

import CardIcon from "../../images/CardIcon.png"

const Card = () => {

  const handleClick = () => {
   console.log(`In Card Click Handler`)
   return true
  }

  return(
   <button href="#" onClick={handleClick}>
     <img alt="Card Icon" src={CardIcon} /> 
   </button>
  )
}

export default Card
