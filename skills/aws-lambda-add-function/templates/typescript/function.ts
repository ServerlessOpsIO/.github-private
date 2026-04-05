/**
 * {{ function_name }} handler
 *
 * {{ description }}
 */

import {
    Context
} from 'aws-lambda'
import {
    Logger
} from '@aws-lambda-powertools/logger'

// Initialize Logger
const LOGGER = new Logger()


/**
 * Main execution
 *
 * @param {{ variable_name }} {{{ variable_data_type }}} - {{ data_description }}
 *
 * @returns {{{ return_type }}} {{ return_value_description }}
 */
export async function main({{ variable_name }}: {{ variable_data_type }}): Promise<{{ return_type }}> {


/**
 * Event handler
 *
 * @param event {{{ variable_data_type }}}- Event
 * @param _ {Context} - Lambda runtime context
 *
 * @returns {{{ return_type }}} {{ return_value_description }}
 */
    export async function handler(event: {{ event_source_type }}, _: Context): Promise<{{ return_type }}> {
    LOGGER.debug('Received event', { event })

    await main({{ variable_name }})

    return