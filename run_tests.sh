#!/bin/bash
#
# Test runner script for ynab-py.
#
# Usage:
#     ./run_tests.sh              # Run all tests
#     ./run_tests.sh unit         # Run only unit tests (fast)
#     ./run_tests.sh integration  # Run only integration tests
#     ./run_tests.sh coverage     # Run with coverage report
#     ./run_tests.sh quick        # Run unit tests only (same as 'unit')
#     ./run_tests.sh <file>       # Run specific test file
#     ./run_tests.sh --help       # Show this help

set -e

print_header() {
    echo ""
    echo "======================================================================"
    echo "  $1"
    echo "======================================================================"
    echo ""
}

# Parse arguments
MODE="${1:-all}"

if [[ "$MODE" == "--help" || "$MODE" == "-h" || "$MODE" == "help" ]]; then
    sed -n '2,12p' "$0" | sed 's/^# //'
    exit 0
fi

# Check if pytest is installed
if ! command -v pytest &> /dev/null; then
    echo "❌ pytest is not installed!"
    echo ""
    echo "Install dependencies:"
    echo "  pip install -r requirements.txt"
    exit 1
fi

# Build pytest command based on mode
case "$MODE" in
    unit|mock|mocked|quick)
        print_header "Running Unit Tests (Fast)"
        pytest tests/ -v -m unit --cov=ynab_py --cov-report=term-missing
        ;;
    
    integration|live)
        print_header "Running Integration Tests"
        pytest tests/ -v -m integration --cov=ynab_py --cov-report=term-missing
        ;;
    
    coverage|cov)
        print_header "Running All Tests with Coverage"
        pytest tests/ -v --cov=ynab_py --cov-report=term-missing --cov-report=html
        echo ""
        echo "📊 Coverage report generated in htmlcov/"
        echo "   Open htmlcov/index.html in your browser to view"
        ;;
    
    all|"")
        print_header "Running All Tests"
        pytest tests/ -v --cov=ynab_py --cov-report=term-missing
        ;;
    
    slow)
        print_header "Running Slow Tests"
        pytest tests/ -v -m slow --cov=ynab_py --cov-report=term-missing
        ;;
    
    *)
        # Assume it's a file path or specific test
        if [[ -f "$MODE" || "$MODE" == tests/* || "$MODE" == *::* ]]; then
            print_header "Running Specific Tests: $MODE"
            pytest "$MODE" -v --cov=ynab_py --cov-report=term-missing
        else
            echo "❌ Unknown mode: $MODE"
            echo ""
            echo "Run './run_tests.sh --help' for usage information"
            exit 1
        fi
        ;;
esac

# Print summary
echo ""
echo "✅ Tests completed successfully!"
echo ""
