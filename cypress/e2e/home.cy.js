describe('Prueba de inicio de sesión en Odoo', () => {
  
  // Esta función se ejecutará antes de cada test (it())
  beforeEach(() => {
    // Llamar al comando login personalizado
    cy.visit('http://localhost:8069/web?db=productos'); // Reemplaza con la URL de tu Odoo

     // Llenar el campo de usuario
     cy.get('input[name="login"]').type('sopanasiuk@d2plus.com'); // Reemplaza con el nombre de tu campo de usuario y credenciales

     // Llenar el campo de contraseña
     cy.get('input[name="password"]').type('Odoo2025_'); // Reemplaza con el nombre de tu campo de contraseña

     // Hacer clic en el botón de inicio de sesión
     cy.get('button.btn.btn-primary').click(); // Asegúrate de que este selector apunte al botón correcto
  });

  it('Debería iniciar sesión correctamente con credenciales válidas', () => {
    cy.contains('Iniciar sesión').should('not.exist');
  });

  /////////////////////////////////////////////////////////////////////
  // cargar productos en la url
  
  it('Debería cargar la página de productos correctamente después de iniciar sesión y verificar la URL', () => {
    cy.visit('http://localhost:8069/mitienda/productos');
    cy.contains('productos').should('exist');
  });

  /////////////////////////////////////////////////////////////////////
  // filtrar por precio
  it('Debería filtrar productos por "Menos de 20€"', () => {
    cy.visit('http://localhost:8069/mitienda/productos');
    cy.get('select[name="precio"]').select('Menos de 20€');
    cy.get('.card-body').should('have.length', 3);
  });

  /////////////////////////////////////////////////////////////////////
  // filtrar por categoria
  it('Debería filtrar productos por categoria ordenador', () => {
    cy.visit('http://localhost:8069/mitienda/productos');
    cy.get('select[name="categoria"]').select(2);
    cy.get('.card-body').should('have.length', 1);
  });
});
