

// Mock clients

// Function under test
import * as func from './function.js'

// Patch any values in function as needed.
jest.mock('./function.js', () => {
    return {
        ...jest.requireActual('./function.js'),
    }
})

describe('{{ function_name }}', () => {
    beforeEach(() => {})

    afterEach(() => {})

    describe('main()', () => {
        beforeEach(() => {})

        describe('should succeed when', () => {
            test('case 1', async () => {})
            test('case 2', async () => {})
        })

        describe('should fail when', () => {
            test('case 1', async () => {})
            test('case 2', async () => {})
        })
    })


    describe('handler()', () => {

        beforeEach(() => {})

        describe('should succeed when', () => {
            test('case 1', async () => {})
            test('case 2', async () => {})
        })

        describe('should fail when', () => {
            test('case 1', async () => {})
            test('case 2', async () => {})
        })
    })
})