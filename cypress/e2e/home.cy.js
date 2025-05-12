describe('Prueba de inicio de sesión en Odoo', () => {
  it('Debería iniciar sesión correctamente con credenciales válidas', () => {
    // Visitar la página de inicio de sesión de Odoo
    cy.visit('http://localhost:8069/web?db=productos'); // Reemplaza con la URL de tu Odoo

    // Llenar el campo de usuario
    cy.get('input[name="login"]').type('sopanasiuk@d2plus.com'); // Reemplaza con el nombre de tu campo de usuario y credenciales

    // Llenar el campo de contraseña
    cy.get('input[name="password"]').type('Odoo2025_'); // Reemplaza con el nombre de tu campo de contraseña

    // Hacer clic en el botón de inicio de sesión
    cy.get('button.btn.btn-primary').click(); // Asegúrate de que este selector apunte al botón correcto

    cy.contains('Iniciar sesión').should('not.exist')
  });

  /////////////////////////////////////////////////////////////////////
  // cargar productos en la url
  it('Debería cargar la página de productos correctamente después de iniciar sesión y verificar la URL', () => {
    //inicia sesion 
    cy.visit('http://localhost:8069/web?db=productos'); // Reemplaza con la URL de tu Odoo
 
    cy.get('input[name="login"]').type('sopanasiuk@d2plus.com'); // Reemplaza con el nombre de tu campo de usuario y credenciales
 
    cy.get('input[name="password"]').type('Odoo2025_'); // Reemplaza con el nombre de tu campo de contraseña

    // Hacer clic en el botón de inicio de sesión
    cy.get('button.btn.btn-primary').click(); 

    // Esperar a que la URL de la página de productos esté disponible
    cy.visit('http://localhost:8069/mitienda/productos')
 
    cy.contains('productos').should('exist'); // Verifica que el texto 'productos' esté en la página
  });

  /////////////////////////////////////////////////////////////////////
  // filtrar por precio

  it('Debería filtrar productos por "Menos de 20€"', () => {
    //inicia sesion 
    cy.visit('http://localhost:8069/web?db=productos'); // Reemplaza con la URL de tu Odoo

    cy.get('input[name="login"]').type('sopanasiuk@d2plus.com'); // Reemplaza con el nombre de tu campo de usuario y credenciales
 
    cy.get('input[name="password"]').type('Odoo2025_'); // Reemplaza con el nombre de tu campo de contraseña

    // Hacer clic en el botón de inicio de sesión
    cy.get('button.btn.btn-primary').click(); 

    // Esperar a que la URL de la página de productos esté disponible
    cy.visit('http://localhost:8069/mitienda/productos')
    
    // Seleccionar el filtro "Menos de 20€" en el formulario
    cy.get('select[name="precio"]')
      .select('Menos de 20€');  // Asegúrate de que el texto coincida con el valor del filtro

    cy.get('.card-body').should('have.length', 3);
   });

  /////////////////////////////////////////////////////////////////////
  // filtrar por categoria

   it('Debería filtrar productos por categoria perifericos', () => {
    //inicia sesion 
    cy.visit('http://localhost:8069/web?db=productos'); // Reemplaza con la URL de tu Odoo

    cy.get('input[name="login"]').type('sopanasiuk@d2plus.com'); // Reemplaza con el nombre de tu campo de usuario y credenciales
 
    cy.get('input[name="password"]').type('Odoo2025_'); // Reemplaza con el nombre de tu campo de contraseña

    // Hacer clic en el botón de inicio de sesión
    cy.get('button.btn.btn-primary').click(); 

    // Esperar a que la URL de la página de productos esté disponible
    cy.visit('http://localhost:8069/mitienda/productos')
    
    // Seleccionar el filtro "Menos de 20€" en el formulario
    cy.get('select[name="categoria"]')
      .select(1);  // Asegúrate de que el texto coincida con el valor del filtro

    cy.get('.card-body').should('have.length', 2);
   });
});