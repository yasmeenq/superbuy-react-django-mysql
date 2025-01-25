import css from "./Products.module.css";
import axios from 'axios';
import { useState, useEffect } from 'react';

export function Products(): JSX.Element {

    const [products, setProducts] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/products/')
            .then((response) => {
                setProducts(response.data);
            })
            .catch((error) => {
                console.error('Error fetching products:', error);
            });
    }, []);

    return (
        <div className={css.Products}>
            {products.map((product) => (
                <div key={product.id} >
                    <img src={product.thumbnail} alt={product.title} />
                    <h3>{product.title}</h3>
                    <p>{product.description}</p>
                    <p>${product.price}</p>
                </div>
            ))}
        </div>
    );
}
