import HelloWorld from '../../src/components/HelloWorld.vue'
const mountVue = require('cypress-vue-unit-test')
<<<<<<< HEAD
describe('HelloWorld', () => {
  beforeEach(mountVue(HelloWorld))

  it('Users H1', () => {
    cy.get('h1').should('contain', 'Users')
  })
})
=======
describe('HelloWorld.vue', () => {
  beforeEach(mountVue(HelloWorld))

  it('Should display the main headline.', () => {
    // By using `data-qa` selectors, we can separate
    // CSS selectors used for styling from those used
    // exclusively for testing our application.
    // See: https://docs.cypress.io/guides/references/best-practices.html#Selecting-Elements
     cy.get('h1').should('contain', 'Users')
  });
});
>>>>>>> a81c92797332c06ef3738ed629d5295cb442ca3c
