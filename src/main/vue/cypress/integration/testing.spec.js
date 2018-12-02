import HelloWorld from '../../src/components/HelloWorld.vue'
const mountVue = require('cypress-vue-unit-test')
describe('HelloWorld', () => {
  beforeEach(mountVue(HelloWorld))

  it('Users H1', () => {
    cy.get('h1').should('contain', 'Users')
  })
})