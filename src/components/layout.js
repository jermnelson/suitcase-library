import React from "react"
import { Link } from "gatsby"

import CatalogNavigation from "../components/catalog-nav"

const Layout = ({ children }) => {
  return(<>
    <CatalogNavigation />
    <div>{children}</div>
  </>)
}

export default Layout
