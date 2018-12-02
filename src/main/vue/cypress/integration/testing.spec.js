import HelloWorld from '../../src/components/HelloWorld.vue'
const mountVue = require('cypress-vue-unit-test')
describe('HelloWorld', () => {
  beforeEach(mountVue(HelloWorld))

  it('Users H1', () => {
    cy.get('h1').should('contain', 'Users')
  })
  it('Read table length', () => {
    cy.get('table tr').should('have.length', 7)
  })
  it('Read Users', () => {
    cy.get('tbody>tr').eq(0).should('contain', 'gsingh@student.tgm.ac.at')
  })
})
