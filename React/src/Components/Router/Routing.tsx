import { Route, Routes } from "react-router-dom";
import "./Routing.css";
import { Products } from "../ProuductsArea/Products/Products";
import { ProductDetails } from "../ProuductsArea/ProductDetails/ProductDetails";
import { HomeArea } from "../HomeArea/HomeArea";

export function Routing(): JSX.Element {
  return (
    <div className="Routing">
      <Routes>
        <Route path="/" element={<HomeArea />}></Route>
        <Route path="/home" element={<HomeArea />}></Route>
        <Route path="/products" element={<Products />}></Route>
        <Route path="/products/:id" element={<ProductDetails />}></Route>
      </Routes>
    </div>
  );
}
