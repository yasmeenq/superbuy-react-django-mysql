import css from "./Products.module.css";
import { useState, useEffect } from "react";
import { productService } from "../../../Services/ProductService";
import { ProductModel } from "../../../Models/ProductModel";
import toast from "react-hot-toast";

export function Products(): JSX.Element {
  const [products, setProducts] = useState<ProductModel[]>([]);

  useEffect(() => {
    async function getProducts() {
      try {
        const dbProducts = await productService.getAllProducts();
        await setProducts(dbProducts);
      } catch (err: any) {
        toast.error(err);
      }
    }
    getProducts();
  }, []);

  return (
    <div className={css.Products}>

      <div className={css.productsList}>
        {products.map((product) => (
          <div key={product.id} className={css.productCard}>
            <img src={product.thumbnail} alt={product.title} />
            <h3>{product.title}</h3>
            <p>{product.description}</p>
            <p>${product.price}</p>
          </div>
        ))}
      </div>

    </div>
  );
}
