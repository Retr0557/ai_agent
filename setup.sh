#!/bin/bash
# Helper script for Prompt Optimizer

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${CYAN}"
echo "========================================"
echo "  🤖 Prompt Optimizer - Helper Script"
echo "========================================"
echo -e "${NC}"

# Function to check if Python is installed
check_python() {
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}❌ Python 3 is not installed${NC}"
        echo "Please install Python 3.8 or higher"
        exit 1
    fi
    echo -e "${GREEN}✓ Python 3 found$(python3 --version 2>&1)${NC}"
}

# Function to install dependencies
install_deps() {
    echo -e "${CYAN}Installing dependencies...${NC}"
    pip install -r requirements.txt
    echo -e "${GREEN}✓ Dependencies installed${NC}"
}

# Function to run demo
run_demo() {
    echo -e "${CYAN}Running demo...${NC}"
    python3 demo.py
}

# Function to run tests
run_tests() {
    echo -e "${CYAN}Running tests...${NC}"
    python3 test_optimizer.py
}

# Function to run main app
run_app() {
    echo -e "${CYAN}Starting Prompt Optimizer...${NC}"
    python3 main.py
}

# Function to setup environment
setup_env() {
    if [ ! -f .env ]; then
        echo -e "${YELLOW}Creating .env file from template...${NC}"
        cp .env.example .env
        echo -e "${GREEN}✓ .env file created${NC}"
        echo -e "${YELLOW}Please edit .env and add your OpenAI API key${NC}"
    else
        echo -e "${GREEN}✓ .env file already exists${NC}"
    fi
}

# Main menu
show_menu() {
    echo ""
    echo -e "${CYAN}What would you like to do?${NC}"
    echo "1. Install dependencies"
    echo "2. Setup environment (.env file)"
    echo "3. Run demo"
    echo "4. Run tests"
    echo "5. Run the app"
    echo "6. Install and setup (1 + 2)"
    echo "7. Full setup and demo (1 + 2 + 3)"
    echo "8. Exit"
    echo ""
    read -p "Enter your choice (1-8): " choice
    
    case $choice in
        1)
            check_python
            install_deps
            show_menu
            ;;
        2)
            setup_env
            show_menu
            ;;
        3)
            run_demo
            show_menu
            ;;
        4)
            run_tests
            show_menu
            ;;
        5)
            run_app
            show_menu
            ;;
        6)
            check_python
            install_deps
            setup_env
            echo -e "${GREEN}✓ Setup complete!${NC}"
            show_menu
            ;;
        7)
            check_python
            install_deps
            setup_env
            echo -e "${GREEN}✓ Setup complete! Running demo...${NC}"
            run_demo
            show_menu
            ;;
        8)
            echo -e "${CYAN}Goodbye! 👋${NC}"
            exit 0
            ;;
        *)
            echo -e "${RED}Invalid choice${NC}"
            show_menu
            ;;
    esac
}

# If script is run with an argument, execute that command directly
if [ $# -gt 0 ]; then
    case $1 in
        install)
            check_python
            install_deps
            ;;
        setup)
            setup_env
            ;;
        demo)
            run_demo
            ;;
        test)
            run_tests
            ;;
        run)
            run_app
            ;;
        *)
            echo -e "${RED}Unknown command: $1${NC}"
            echo "Usage: $0 [install|setup|demo|test|run]"
            exit 1
            ;;
    esac
else
    show_menu
fi
