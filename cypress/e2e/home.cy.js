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
  it('Debería cargar la página de productos correctamente después de iniciar sesión y verificar la URL', () => {
    
    cy.visit('http://localhost:8069/web?db=productos'); // Reemplaza con la URL de tu Odoo

    // Llenar el campo de usuario
    cy.get('input[name="login"]').type('sopanasiuk@d2plus.com'); // Reemplaza con el nombre de tu campo de usuario y credenciales

    // Llenar el campo de contraseña
    cy.get('input[name="password"]').type('Odoo2025_'); // Reemplaza con el nombre de tu campo de contraseña

    // Hacer clic en el botón de inicio de sesión
    cy.get('button.btn.btn-primary').click(); 

    // Esperar a que la URL de la página de productos esté disponible
    cy.visit('http://localhost:8069/mitienda/productos')
    
    // También puedes agregar una comprobación de la palabra 'productos' en el contenido de la página
    cy.contains('productos').should('exist'); // Verifica que el texto 'productos' esté en la página
  });
});