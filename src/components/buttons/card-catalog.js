import React from "react"

import CardFile from "../../images/CardFile.png"

const CardCatalog = () => {

  const handleClick = () => {
   return (alert('Browse the Catalog'))

  }

  return(
   <button href="#" onClick={handleClick}>
     <img alt="Card Catalog Icon" src={CardFile} /> 
   </button>
  )
}

export default CardCatalog
