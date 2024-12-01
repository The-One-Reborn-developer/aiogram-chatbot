from app.scripts.pass_evaluation_to_model import pass_evaluation_to_model


assert pass_evaluation_to_model(
    question='What is the base URL for Testnet?',
    expected_response='https://testnet-pay.crypt.bot/'
)

assert pass_evaluation_to_model(
    question='What is the base URL for Mainnet?',
    expected_response='https://pay.crypt.bot/'
)

assert pass_evaluation_to_model(
    question='How can the application receive payments?',
    expected_response='Invoice'
)

assert pass_evaluation_to_model(
    question='How can the application send payments?',
    expected_response='transfer'
)

assert pass_evaluation_to_model(
    question='How to test authentication?',
    expected_response='getMe'
)

assert pass_evaluation_to_model(
    question='How to create a check',
    expected_response='createCheck'
)