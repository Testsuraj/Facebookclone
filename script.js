// script.js
document.addEventListener('DOMContentLoaded', function() {
  // Products are already loaded from products.js
  displayProducts(products);
});

function displayProducts(products) {
  const tableBody = document.getElementById('home_page_product');
  tableBody.innerHTML = ''; // Clear existing content

  // Loop through products and create rows (2 products per row)
  for (let i = 0; i < products.length; i += 2) {
    const row = document.createElement('tr');
    
    // Add first product in row
    if (products[i]) {
      row.appendChild(createProductCell(products[i]));
    }

    // Add second product in row (if exists)
    if (products[i + 1]) {
      row.appendChild(createProductCell(products[i + 1]));
    }

    tableBody.appendChild(row);
  }
}

// Helper function to create a product cell
function createProductCell(product) {
  const cell = document.createElement('td');
  cell.className = 'Cs7ycL TcKeCe';
  
  cell.innerHTML = `
    <a href="${product.id}">
      <div class="_2enssu">
        <div style="position:relative;min-height:170px;min-width:170px">
          <div class="_3LXIRu">
            <div class="_2GaeWJ" style="width:170px;height:170px">
              <img class="_2puWtW _3a3qyb" src="${product.image}" alt="${product.name}">
            </div>
          </div>
        </div>
        <div class="_24B_AU _3SexMn">${product.name}</div>
        <div class="_24B_AU _1AQnZC">
          ${product.discount}
          <span class="mrp">${product.mrp}</span>
        </div>
        <div class="_24B_AU _1AQnZC">
          <b class="selling-price">${product.price}</b>
          <img src="img/SwOvZ3r.png" width="77px">
        </div>
        <div class="_24B_AU _1AQnZC">
          <b class="_3LWZlK">${product.rating} <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==" class="_1wB99o"></b>
        </div>
        <div class="_3Nxu4r delivery-txt">${product.delivery}</div>
      </div>
    </a>
  `;
  
  return cell;
}
