import HelloWorld from '../../src/components/HelloWorld.vue'
const mountVue = require('../../src')

/* eslint-env mocha */
describe('HelloWorld.vue', () => {
  beforeEach(mountVue(HelloWorld))

  it('shows Users', () => {
    cy.contains('Users')
  })
})

describe('Several components', () => {
  const template = `
          <thead>
            <tr>
              <th scope="col">Username</th>
              <th scope="col">Email</th>
              <th scope="col">Picture</th>
            </tr>
          </thead>
  `
  const components = {
    hello: Hello
  }
  beforeEach(mountVue({ template, components }))

  it('greets the world 3 times', () => {
    cy.get('p').should('have.length', 1)
  })
})
