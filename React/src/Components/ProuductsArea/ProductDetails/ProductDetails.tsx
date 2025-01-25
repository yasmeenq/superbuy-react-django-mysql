import { useParams } from "react-router-dom";
import css from "./ProductDetails.module.css";

export function ProductDetails(): JSX.Element {
  const params = useParams();
  if (params.id) {
    const id = params.id;
  }

  return <div className={css.ProductDetails}>

    
  </div>;
}
