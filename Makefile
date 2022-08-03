# *********************************************************
#                    RPM Build
# *********************************************************
NAME            := catppuccin-gtk
VERSION         := 0.2.5
RELEASE         := 1
GIT_TAG         := v-0.2.5
ROOT_DIR        := $(shell pwd)
RPM_BUILDDIR    := $(ROOT_DIR)/rpmbuild
RPM_BUILD_FLAGS := --define "_release $(RELEASE)" --define "_version $(VERSION)" --define "_gittag $(GIT_TAG)"
RPM_BUILD_FLAGS += --define "_topdir $(RPM_BUILDDIR)" --define "_name $(NAME)"
RPM_SPECFILE    := $(NAME).spec
RPM_SOURCE      := $(RPM_BUILDDIR)/SOURCES/*.zip
RPM_FILES       := $(ROOT_DIR)/RPMS/*.rpm
GDM_FILE        := gnome-shell-theme.gresource.xml

ORANGE = \e[0;33m
GREEN = \e[0;32m
END = \e[0m

.PHONY: clean clean_all help

define help_text
Targets:
  - make rpm:       Create RPMs.
  - make clean:     Clean up build generated artifacts.
  - make clean_all: Delete everything, including the built RPMs.
  - make [help]:    Print this help.
endef
export help_text

help:
	@echo "$$help_text"

# Create the source input.
$(RPM_SOURCE): $(GDM_FILE)
	@echo -e "${ORANGE}Downloading source files...${END}"
	@mkdir -p $(RPM_BUILDDIR)/SOURCES
	@spectool --sourcedir --get-files $(RPM_BUILD_FLAGS) $(RPM_SPECFILE) >/dev/null
	@cp $(GDM_FILE) $(RPM_BUILDDIR)/SOURCES/$(GDM_FILE)

# Build the RPM.
$(RPM_FILES): $(RPM_SOURCE)
	@echo -e "${ORANGE}Building rpm...${END}"
	@rm -rf $(RPM_BUILDDIR)/BUILD $(RPM_BUILDDIR)/BUILDROOT
	@rpmbuild --quiet -bb $(RPM_BUILD_FLAGS) $(RPM_SPECFILE)
	@mkdir -p $(ROOT_DIR)/RPMS
	@cp -r $(RPM_BUILDDIR)/RPMS/noarch/*.rpm $(ROOT_DIR)/RPMS/
	@chmod 744 $(ROOT_DIR)/RPMS/*

clean:
	@echo -e "${GREEN}Deleting:${END} $(RPM_BUILDDIR)"
	@rm -rf $(RPM_BUILDDIR)

clean_all:
	@echo -e "${GREEN}Deleting:${END} $(RPM_BUILDDIR)"
	@rm -rf $(RPM_BUILDDIR)
	@echo -e "${GREEN}Deleting:${END} $(RPM_FILES)"
	@rm -rf $(RPM_FILES)

rpm: $(RPM_FILES)
	@echo -e "${GREEN}Build is complete:${END} $(RPM_FILES)"
